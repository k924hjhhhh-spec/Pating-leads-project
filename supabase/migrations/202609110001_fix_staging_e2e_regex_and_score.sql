create or replace function public.painting_leads_staging_e2e(payload jsonb)
returns jsonb
language plpgsql
security definer
set search_path to 'pg_catalog', 'public', 'painting_leads'
as $function$
declare
  jwt_role text := coalesce(current_setting('request.jwt.claim.role', true), (nullif(current_setting('request.jwt.claims', true),'')::jsonb->>'role'), '');
  lid uuid := gen_random_uuid();
  cid uuid := gen_random_uuid();
  did uuid := gen_random_uuid();
  aid uuid := gen_random_uuid();
  fid uuid := gen_random_uuid();
  sid uuid := gen_random_uuid();
  idem uuid;
  phone text;
  email text;
  zipc text;
  origin text := payload->>'origin';
  scheduled timestamptz;
  v_score int;
  ev jsonb;
begin
  if jwt_role <> 'service_role' then raise exception 'not authorized'; end if;
  if not exists(select 1 from painting_leads.environment_identity where id=1 and project='Painting Leads' and environment='staging' and live_enabled=false) then raise exception 'unsafe environment'; end if;
  if (select count(*) from painting_leads.leads) <> 0 or (select count(*) from painting_leads.contractors) <> 0 then raise exception 'E2E already executed or database not empty'; end if;

  if payload->>'customer_name' <> 'FICTIONAL Pilot Test' then raise exception 'fictional test name required'; end if;
  phone := regexp_replace(coalesce(payload->>'phone',''), '\D','','g');
  if length(phone)=11 and left(phone,1)='1' then phone:=substr(phone,2); end if;
  if length(phone)<>10 or substr(phone,4,3)<>'555' or right(phone,4)::int not between 100 and 199 then raise exception 'fictional phone required'; end if;
  email := lower(payload->>'email'); if email !~ '^[^@[:space:]]+@example\.com$' then raise exception 'example.com required'; end if;
  zipc := payload->>'zip'; if zipc not in ('33060','33064','33062') then raise exception 'pilot zip only'; end if;
  if payload->>'property_type'<>'residential' or payload->>'service_type'<>'interior' then raise exception 'pilot scope only'; end if;
  if coalesce((payload->>'consent')::boolean,false) is not true or payload->>'consent_policy_version'<>'staging-v1' then raise exception 'consent required'; end if;
  if length(coalesce(payload->>'notes',''))<10 then raise exception 'notes required'; end if;
  idem := (payload->>'idempotency_key')::uuid;
  scheduled := now()+interval '1 day';

  insert into painting_leads.contractors(id,business_name,status,service_zips,specialties,available_until,identity_verified,insurance_expires,license_check,license_reason,portfolio_verified,communication_verified,terms_version,terms_accepted_at,reviewed_by,reviewed_at,evidence)
  values(cid,'FICTIONAL STAGING CONTRACTOR','approved',array[zipc],array['interior'],now()+interval '7 days',true,current_date+30,'not_applicable','Fictional scenario only',true,true,'fixture-only-v1',now(),'staging-fixture',now(),'{"simulated":true}'::jsonb);

  insert into painting_leads.leads(id,idempotency_key,request_hash,customer_name,phone,email,zip,property_type,service_type,rooms_or_sqft,requested_timeline,notes,consent_at,consent_policy_version,status)
  values(lid,idem,md5(payload::text),payload->>'customer_name','+1'||phone,email,zipc,'residential','interior',payload->>'rooms_or_sqft',payload->>'requested_timeline',payload->>'notes',now(),'staging-v1','new');
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'ALEX','alex.intake_completed',null,'new','{"simulated":true,"external_action":false}');

  v_score := 60 + case when payload->>'requested_timeline' in ('ASAP','2 weeks') then 20 else 0 end + case when length(payload->>'notes')>=20 then 20 else 0 end;
  update painting_leads.leads set score=v_score,score_reason='Rules-v1 fixture score',status='qualified',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'MAX','max.staging_completed','new','qualified','{"simulated":true,"external_action":false}');

  insert into painting_leads.job_cards(id,lead_id,scope) values(gen_random_uuid(),lid,jsonb_build_object('lead_id',lid,'location',jsonb_build_object('zip',zipc,'city',payload->>'city'),'service','interior','scope',payload->>'rooms_or_sqft','photos',jsonb_build_array(),'urgency',payload->>'requested_timeline','estimated_range',null,'confidence','not_available_no_approved_pricing','missing_data',jsonb_build_array(),'status','job_card_ready','timestamp',now(),'condition',payload->>'condition','areas',payload->>'areas'));
  update painting_leads.leads set status='job_card_ready',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'RYAN','ryan.staging_completed','qualified','job_card_ready','{"simulated":true,"external_action":false}');

  insert into painting_leads.matches(lead_id,contractor_id,rank,reasons) values(lid,cid,1,'["ZIP","specialty","approval","availability","insurance"]'::jsonb);
  update painting_leads.leads set status='matching',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'LUCAS','lucas.staging_completed','job_card_ready','matching','{"simulated":true,"external_action":false}');

  insert into painting_leads.distributions(id,lead_id,contractor_id,state,response_deadline) values(did,lid,cid,'held',now()+interval '15 minutes');
  update painting_leads.leads set status='distributed',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'JACK','jack.staging_completed','matching','distributed','{"simulated":true,"external_action":false,"distribution":"held"}');

  update painting_leads.distributions set state='accepted',responded_at=now() where id=did;
  insert into painting_leads.appointments(id,lead_id,contractor_id,scheduled_at,homeowner_confirmed_at,contractor_confirmed_at,state) values(aid,lid,cid,scheduled,now(),now(),'confirmed');
  update painting_leads.leads set status='appointment_set',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'LEO','leo.staging_completed','distributed','appointment_set','{"simulated":true,"external_action":false,"followup_sent":false}');

  update painting_leads.appointments set state='completed' where id=aid;
  insert into painting_leads.fee_events(id,lead_id,outcome) values(fid,lid,'won');
  update painting_leads.leads set status='won',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'ETHAN','ethan.staging_completed','appointment_set','won','{"simulated":true,"external_action":false,"money_moved":false}');

  insert into painting_leads.sam_performance_records(id,lead_id,contractor_id,feedback,rating,complaint) values(sid,lid,cid,'Fictional successful job feedback',5,false);
  update painting_leads.leads set status='closed',updated_at=now() where id=lid;
  insert into painting_leads.lead_events(lead_id,worker,event_type,from_status,to_status,payload) values(lid,'SAM','sam.staging_completed','won','closed','{"simulated":true,"external_action":false,"review_sent":false,"referral_sent":false}');

  select jsonb_agg(jsonb_build_object('worker',worker,'event_type',event_type,'from',from_status,'to',to_status) order by id) into ev from painting_leads.lead_events where lead_id=lid;
  return jsonb_build_object('status','PASS','lead_id',lid,'final_status','closed','events',ev,'messages_sent',0,'money_moved',false,'ads_published',0,'real_pilot_ready',false,'origin','simulated_fixture','staging_origin',origin);
end;
$function$;

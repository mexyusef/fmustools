# Objective

kita penasaran ini gak pernah sampai tercapai.
langkah awal: kumpulkan dulu model

## coba bandingkan dg assignment berikut:
ini utk melamar di crossover...

ATTENTION! YOUR APPLICATION WILL BE REJECTED IF IT:
- Does not compile
- Does not contain unit tests
- Unit tests are failing

Requirements:
Objective
Create a public news publishing portal where news can be published and disseminated

Instructions:
- Try to complete as much as possible within the given time frame. 
If you need more time, please ask for an extension. 
You must complete full-functionality of the application 
  with industry-level coding style/commenting. 
Unfinished assignments will not be considered.
- Please note that you are expected to work on the assignment independently. 
Discussing assignment details with colleagues or any indication of outside help 
  will be considered cheating.
- Please do not expect too much hand-holding as this is an evaluation assignment.
- Read the complete assignment before you start. 
  Understand clearly what is required so that your work will be appropriate and easier.

Preconditions
- You should work on your local machine.
- You may use any IDE or editor for developing the application.
- You must use the latest PHP7 version compatible with required libraries.
- You must use Nginx or Apache or IIS as the web server.
- You must use MySQL as database.
- You must use one of these frameworks:
  Laravel
  CodeIgniter
  Yii2
  Symfony2
- Failing to follow these rules will invalidate your submission and you will not be evaluated.

Delivery for this assignment should consist of an archive named <your_name> - Software Engineer - PHP.zip
containing the following:
- Source code/project
  Application Demo
  - Record the demonstration of the application using Wink. Do not upload the video. Save it to your local machine.
  Database script
  - Create a single SQL script file to create the database, its schema and any stored procedure you may use.
- Wink recording, download version 2 from Wink, render the video to swf format
- Readme.txt containing the instructions to configure and run the application, notes and feedback
  Readme
  - Create a txt file with the following information
  - Steps to create and initialize the database
  - Steps to prepare the source code to build/run properly
  - Any assumptions made and missing requirements that are not covered in the specifications
  - Any feedback you may wish to give about improving the assignment
- Design.doc with needed diagrams
  Design diagrams
  - Create a doc file containing the following information and diagrams
  - List of technologies and design patterns used
  - An overall activity or sequence diagram
  - An overall layer or component interaction diagram

To be evaluated
1. The quality of the output (functionality)
2. Code quality and completeness
3. Technologies applied
4. Extra validations and assumptions which are not described
5. Add missing requirements to the implementation, according to your experience

Technical Specifications
- Use MVC design.
- Use MySQL database. Create the needed tables.
- Use a PDF export library.
- Create a single application with the publishing, newsstand and RSS service.
- Use PHP Mailer as mailing library.
- Apply input validations and constraints wherever necessary to create a stable application.
- Even if you are not able to complete all the tasks, try to achieve a working application.

Functional Specifications
Create a public news publishing system where people can report or read news
I. News publishing web application
I.1 Any user could register with an email address. 
The application sends a verification link to the email address. 
When the user clicks the link, the application asks for a new password 
  (can be tested on localhost w/o need for a public domain). 
Now the user is registered and is able to publish news. 
Without this verification user cannot publish news.

I.2 After log in the user could see his own published news list, remove or publish a new article.
No edit of news is permitted.

I.3 For each news article the following information is required
  I.3.1 News title
  I.3.2 A single photo
  I.3.3 News text
  I.3.4 Current date and time
  I.3.5 Reporter user name / email

I.4 Newsstand web application available w/o log in for general public
  I.4.1 Users could see the news highlights. Latest 10 news only.
  I.4.2 Upon clicking an article highlight, the user is able to view a complete article.
  I.4.3 The user is able to download a PDF file of the displayed news article.

I.5 A News RSS feed service
  I.5.1 An RSS feed can be subscribed to, which includes latest 10 news articles

## arsip

## SOP

## SPOR/SUCOR

Admin
  email,s,N
  password,i,N
  refresh_token,s
  permissions,s
AdvisorActivity
  advisor_id,i,N
  user_id,s
  activity_type,s
  notes,s
  created_at,ts
Bank
  no,i,N
  account,s
  bi_member_code,s
  member_name,s
  display_name,s
  Bank.removeAttribute("id");
BoMasterValue
  identity,s
  type,s
  descone,s
  desctwo,s
  code,s
DailyNav
  closedate,ts,N
  fundcode,s,N
  nav,f
  aumamount,f
  outstandingunit,f
  cashamount,f
  
  File
    fieldname,s
    originalname,s
    encoding,s
    mimetype,s
    destination,s
    filename,s
    path,s
    size,bi
    timestamp,ts
    id_user,bi
    type,s,(fotoselfie,fotoektp,tandatangan)

  Fund
    fundcode,s,N
    fundname,s
    fundtype,s
    kpd,s
    currency,s
    issueddate,ts
    closedate,ts
    custodiancode,s
    onlinetrading,s
    fund_pasar_dana_id,i
    investment_manager_id,i
    Fund.removeAttribute("id");
  FundOrder
    orderno,bi,pk,ai
    customerno,bi
    fundcode,s,N,
      references: "m_fund",
      referencesKey: "fundcode",
      spt nya ini foreign key ke table m_fund dan column fundcode
    orderdate,ts
    orderstatus,s,(U,N,L,O,C,W,R)
        "U", // Unverified, from advisor nedd verification from client
        "N", // New
        "L", // Load
        "O", // Approved
        "C", // Complete
        "W", // Withdraw
        "R", // Rejected
    transactiontype,s,(S,R,SW) // Subs, Redeem, Switch
    transactionid,bi
    transactionfee,n
    redeemtype,s,(A,U,T) // Amount, Unit, All Unit
    orderunit,f
    orderamount,f
    ordernav,f
    feetype,s
    processdate,ts
    fundcodeswitch,s
    notes,s
    sign_url,s
    sign_doc_url,s
    mean_nav,f
    FundOrder.hasOne(Fund, {
      foreignKey: "fundcode",
      sourceKey: "fundcode",
    });
    FundOrder.hasOne(Product, {
      foreignKey: "fundcode",
      sourceKey: "fundcode",
    });
    FundOrder.hasOne(Transaction, {
      foreignKey: "id",
      sourceKey: "transactionid",
    });
  FundSummary
    customerno,s,N
    fundcode,s,N
    unit,f
    averageprice,f
  Kyc
    type,i
    sa_code,s
    sid,s
    firstname,s
    middlename,s
    lastname,s
    cc_nationality,s
    id_no,s
    id_expiry_date,s
    npwp_no,s
    npwp_reg_date,s
    cc_birth,s
    place_birth,s
    date_birth,s
    gender,i
    education_code,i
    mother_name,s
    religion_code,i
    occupation_code,i
    income_code,i
    marital_code,i
    spouse_name,s
    risk_profile_code,i
    investment_obj_code,i
    source_of_fund_code,i
    asset_owner_code,i
    ktp_adress,s
    ktp_city_code,i
    ktp_postal_code,i
    correspondence_address,s
    correspondence_city_code,i
    correspondence_city_name,s
    correspondence_postal_code,i
    correspondence_cc,s
    domicile_address,s
    domicile_city_code,s
    domicile_city_name,s
    domicile_postal_code,s
    domicile_cc,s
    home_phone,s
    mobile_phone,s
    fax,s
    email,s
    statement_type,i
    fatca_status,i
    tin,s
    tin_issuance_cc,s
    redm_payment_bank_bic_code_1,s
    redm_payment_bank_bi_member_code_1,s
    redm_payment_bank_name_1,s
    redm_payment_bank_cc_1,s
    redm_payment_bank_branch_1,s
    redm_payment_ac_ccy_1,s
    redm_payment_ac_no_1,s
    redm_payment_ac_name_1,s
    redm_payment_bank_bic_code_2,s
    redm_payment_bank_bi_member_code_2,s
    redm_payment_bank_name_2,s
    redm_payment_bank_cc_2,s
    redm_payment_bank_branch_2,s
    redm_payment_ac_ccy_2,s
    redm_payment_ac_no_2,s
    redm_payment_ac_name_2,s
    redm_payment_bank_bic_code_3,s
    redm_payment_bank_bi_member_code_3,s
    redm_payment_bank_name_3,s
    redm_payment_bank_cc_3,s
    redm_payment_bank_branch_3,s
    redm_payment_ac_ccy_3,s
    redm_payment_ac_no_3,s
    redm_payment_ac_name_3,s
    client_code,s
    id_user,i
    review,s

    let KycPage2 = require("./KycPage2");
    Kyc.hasOne(KycPage2, {
      foreignKey: "id",
      sourceKey: "id"
    });
KycPage2
  no_ektp_pasangan,s
  nama_ektp_pasangan,s
  tmptlhr_ektp_pasangan,s
  tgllhr_ektp_pasangan,s
  phone_ektp_pasangan,s
  warganegara_ektp_pasangan,s
  pekerjaan_pasangan,s
  bidangusaha_pasangan,s
  bidangusaha,s
  bidangusaha_lainnya,s
  foto_ktp,s
  foto_selfie,s
  foto_tanda_tangan,s
  pekerjaan_lainnya,s
  pekerjaan_pasangan_lainnya,s
  bidangusaha_pasangan_lainnya,i
MarketHoliday
  date,ts
NavCronLog
  fund_id,i
  latest_date_fetch,s
  NavCronLog.removeAttribute("id");
News
  judul,s,N
  tgl,ts,N
  tgl_mulai,ts,
  tgl_selesai,ts,
  gambar,s
  need_login,i
  News.hasOne(NewsDetail, {
    foreignKey: "id_news",
    sourceKey: "id"
  });
NewsDetail
  isi,s,N
  gambar,s
  note,s
  gambar2,s
  gambar3,s
  gambar4,s
  id_news,i
  
  NewsDetail.belongsTo(News, {
    foreignKey: "id_news",
    targetKey: "id"
  });
  isi,s,N
  gambar,s
  note,s
  gambar2,s
  gambar3,s
  gambar4,s
  id_news,i

  Notification,ts
    user_id,bi
    title,s
    content,s
    data_type,s
    data_ref_id,bi
    data_ref_status,s
    is_read,b,df=false
  Otp,ts
    id_user,i,N
    otp,s,N
    purpose,s
    reference_id,s
    expired_at,ts,
  PaymnetMethod
    paymenttype,s,(manual-transfer,virtual-account,gopay,ovo)
    bank,i
    accountref,s
    fundcoderef,s
    PaymentMethod.hasOne(Bank, {
      foreignKey: "no",
      sourceKey: "bank",
    });
  Post,ts
    user_id,bi,N
    content,t
    likes_amount,bi
    comments_amount,bi
    report_amount,bi
    Post.hasOne(User, {
      foreignKey: "id",
      sourceKey: "user_id",
      as: "user",
    });
    Post.hasOne(PostReference, {
      foreignKey: "post_id",
      sourceKey: "id",
      as: "reference",
    });
  PostComment,ts
    user_id,bi,N
    post_id,bi,N
    content,t
    PostComment.hasOne(User, {
      foreignKey: "id",
      sourceKey: "user_id",
      as: "user",
    });
PostLikes,ts
  user_id,bi,N
  post_id,bi,N
  PostLikes.hasOne(User, {
    foreignKey: "id",
    sourceKey: "user_id",
    as: "user",
  });
PostReference
  post_id,bi,N
  type,s
  reference,s
PostReport,ts
  post_id,bi,N
  user_id,bi,N
  content,t
  PostReport.hasOne(User, {
    foreignKey: "id",
    sourceKey: "user_id",
    as: "user",
  });
Product
  prodname,s
  price,f
  grup,s
  perf_6bln,f
  perf_1thn,f
  perf_3thn,f
  perf_5thn,f
  min_trx,f
  min_portofolio,f
  min_redemption,f
  profil_risiko,f
  metode_pembayran,i
  fundcode,s
  closedate,ts
  lastupdate,ts
  buyable,b
RefCountry
  cc,s
  country,s

  SyaratKetentuan
    text,s
    SyaratKetentuan.removeAttribute("id");
  Transaction,ts
    userid,bi,N
    amount,n
    status,s,(unpaid,rejected,approvated>unpaid)
    paymentid,i
    paymentreference,s
    expired_at,ts
    paid_at,ts
    notes,s
  TransDetail
    customerno,s,N
    transdate,ts
  User
    firstname,s
    lastname,s
    email,s,N
    pwd,s,N
    phone,s,N
    customerno,i
    confirm_code,s
    enabled,i
    activated,i
    progres_registrasi,i
    progres_kyc,i
    fcm_token,s
    flag_login,i
    role,s,(customer,advisor>customer)
    referral_code,s
    referrer_id,s
    profile_image,s
    change_data_info,jsonb
  UserAuthToken
    id_user,i,N
    refresh_token,s,N
    refresh_expired_time,ts,N
UserBank,ts
  user_id,bi
  bank_id,i
  bank_cc,s
  acc_currency,s
  acc_no,s
  acc_holder_name,s
  UserBank.hasOne(Bank, {
    foreignKey: "no",
    sourceKey: "bank_id",
  });
UserLog
  user_id,bi
  ip_address,s
  device_type,s
  device_os,s
  device_agent,s
  full_user_agent,s
  activity,s
  log_at,ts
  data,jsonb
UserProduct,ts
  user_id,bi
  fundcode,s
  unitamount,f
  investamount,f
  last_trans_nav,f
  mean_trans_nav,f
  gain_loss,f
  gain_loss_percent,f
  UserProduct.hasOne(Product, {
    foreignKey: "fundcode",
    sourceKey: "fundcode",
  });
..
..

## whosedoctor

## Vietnam ecommerce

## Proshop django ecommerce

## Mumble

# additional

has_one + belongs_to

has_one:
AnyNode(as_column='user', assoc_table='User', domestic_column='user_id', foreign_column='id', has_or_belongs='has_one', model='PostReport', name='table', remove_attribute_id=True, timestamp=True, type='table')
PostReport.hasOne(User, {
  foreignKey: 'id',
  targetKey: 'user_id',  
  as: 'user',
})

belongs_to:
AnyNode(as_column='user', assoc_table='User', domestic_column='user_id', foreign_column='id', has_or_belongs='belongs_to', model='PostReport', name='table', remove_attribute_id=True, timestamp=True, type='table')
PostReport.belongsTo(User, {
  foreignKey: 'id',
  targetKey: 'user_id',  
})

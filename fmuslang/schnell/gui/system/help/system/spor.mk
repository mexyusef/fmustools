--% data model

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
--#

--% getting started, entry point
ReactDOM.render(<App />, document.getElementById("root"));

import Alert from "./modules-customer/alert/alert";
import Router from "./router";
import Loading from "./modules-customer/loading";
<Loading
component={
  <div className={classes.container}>
    <Router />
    <Alert />
  </div>
}
/>

sementara router berisi:
<Route exact path="/app/login" component={Login} />

<PrivateComponent
exact
path="/app/komunitas"
component={CommunityPage}
/>

dg loadable berisi:
export const Login = Loadable({
  loading,
  loader: () => import("../modules-customer/auth/login"),
});
export const CommunityPage = Loadable({
  loading,
  loader: () => import("modules-customer/community"),
});
--#

--% modules-customer/community/index.js
const {
  posts,
  imageContent,
  activeReportPostID,
  reportContent,
  onPost,
  setPostContent,
  onChangeImage,
  setActiveReportPostID,
  setReportContent,
  onReport,
} = useCommunityHook();

{posts.map((post, key) => (
  <PostItem key={key} {...post} onClickReport={setActiveReportPostID} />
))}
PostItem adlh bagian mendisplay, ada di modules-customer/community/partials/PostItem.js


sedangkan isi dari useCommunityHook:
import { getAllPost, createPost, reportPost } from "fetcher";

const [posts, setPosts] = useState([]);

useEffect(() => {
  getAllPost()
  .then(({ data }) => {
    const { posts } = data;
    setPosts(
      posts.map((_post) => {
        ...
        return _post;
      })
    );
  });
}, []);
--#

--% fetcher/index.js
export * from "./community";

fetcher/community.js
import _req from "common/request";

export const getAllPost = (data = {}) => {
  const { limit, skip } = data;
  return _req.createService(`/post`).get({ limit, skip });
};
--#

--% sporbe, endpoint /post, routes/v2/post.js, controllers/post.js, daos/post.js
const CommunityController = require("../../controllers/post");
const { checkAuthToken } = require("../../middlewares/auth");
module.exports = (express) =>
  express
    .Router()
    .use(checkAuthToken)
    .get("/", CommunityController.getAllPost)
    .get("/:post_id", CommunityController.getPostDetail)
    .post("/", CommunityController.createPost)
    .post("/like/:post_id", CommunityController.likePost)
    .post("/dislike/:post_id", CommunityController.dislikePost)
    .post("/comment/:post_id", CommunityController.commentPost)
    .post("/report/:post_id", CommunityController.reportPost);
kita lihat CommunityController.getAllPost
controllers/post.js
const PostDAOS = require("../daos/post");
const PostBridge = require("../bridges/post");
const getAllPost = async (req, res, next) => {
  const { limit, skip } = await PostBridge.validateGetAllPostRequest(
    req.query
  );
  const posts = await PostDAOS.getAllUserPost(req.user.id_user, {
    limit,
    skip,
  });
  const total = await PostDAOS.countPost({});
  return res.json({
    posts,
    total,
  });
};
kita lihat PostDAOS di daos/post
const Post = require("../models/Post");
exports.getAllUserPost = async (userID, { limit, skip }) => {

  const posts_query = `
  SELECT 
    "sm_posts"."id", 
    "sm_posts"."user_id", 
    "sm_posts"."content", 
    "sm_posts"."likes_amount", 
    "sm_posts"."comments_amount", 
    "sm_posts"."report_amount", 
    "sm_posts"."createdAt", 
    "sm_posts"."updatedAt", 
    "user"."id" AS "user.id", 
    "user"."firstname" AS "user.firstname", 
    "user"."lastname" AS "user.lastname", 
    "user"."email" AS "user.email", 
    "user"."phone" AS "user.phone", 
    "user"."profile_image" AS "user.profile_image", 
    "reference"."id" AS "reference.id", 
    "reference"."post_id" AS "reference.post_id", 
    "reference"."type" AS "reference.type", 
    "reference"."reference" AS "reference.reference"

  FROM "snap_dev"."sm_posts" AS "sm_posts" 
  LEFT OUTER JOIN "snap_dev"."s_users" AS "user" 
    ON "sm_posts"."user_id" = "user"."id" 
  LEFT OUTER JOIN "snap_dev"."sm_post_references" AS "reference" 
    ON "sm_posts"."id" = "reference"."post_id"
  ORDER BY "sm_posts"."createdAt" DESC LIMIT 10 OFFSET 0;
  `;

  return result;
};
--#

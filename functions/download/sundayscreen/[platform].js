import { makeDownloadHandler } from "../_lib.js";
export const onRequest = makeDownloadHandler({ app: "sundayscreen", repo: "SundaySuite-app/sundayscreen", appName: "SundayScreen", macArch: "aarch64", rings: true, hasStableRelease: false });

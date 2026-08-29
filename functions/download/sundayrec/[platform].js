import { makeDownloadHandler } from "../_lib.js";
export const onRequest = makeDownloadHandler({ app: "sundayrec", repo: "SundaySuite-app/sundayrec", appName: "SundayRec", macArch: "aarch64", rings: true, hasStableRelease: true });

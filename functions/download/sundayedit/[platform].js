import { makeDownloadHandler } from "../_lib.js";
export const onRequest = makeDownloadHandler({ app: "sundayedit", repo: "SundaySuite-app/sundayedit", appName: "SundayEdit", macArch: "universal", rings: false, hasStableRelease: true });

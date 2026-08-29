import { makeDownloadHandler } from "../_lib.js";
export const onRequest = makeDownloadHandler({ app: "sundaystage", repo: "SundaySuite-app/sundaystage", appName: "SundayStage", macArch: "aarch64", rings: true, hasStableRelease: true });

import { makeDownloadHandler } from "../_lib.js";
export const onRequest = makeDownloadHandler({ app: "sundaysync", repo: "SundaySuite-app/sundaysync", appName: "SundaySync", macArch: "aarch64", rings: true, hasStableRelease: false });

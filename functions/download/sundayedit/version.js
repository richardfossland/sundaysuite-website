import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundayedit", repo: "richardfossland/sundayedit", rings: false });

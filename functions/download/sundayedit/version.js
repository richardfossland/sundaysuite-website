import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundayedit", repo: "SundaySuite-app/sundayedit", rings: false });

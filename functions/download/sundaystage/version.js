import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundaystage", repo: "SundaySuite-app/sundaystage", rings: true });

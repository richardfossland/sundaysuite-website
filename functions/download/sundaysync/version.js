import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundaysync", repo: "SundaySuite-app/sundaysync", rings: true });

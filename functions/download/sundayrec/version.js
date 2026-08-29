import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundayrec", repo: "SundaySuite-app/sundayrec", rings: true });

import { makeVersionHandler } from "../_lib.js";
export const onRequest = makeVersionHandler({ app: "sundayscreen", repo: "SundaySuite-app/sundayscreen", rings: true });

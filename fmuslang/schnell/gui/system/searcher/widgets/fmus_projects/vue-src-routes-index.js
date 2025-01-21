import { createRouter, createWebHistory } from "vue-router";

const routes = [
{

}
];

function Router() {
    const router = new createRouter({
        history: createWebHistory(),
        routes,
    });
    return router;
}

const router = Router();

export default router;

import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/store/AuthStore";
import { useCampagneStore } from "@/store/CampagneStore";
import Home from "../views/general/Home.vue";
import GetStarted from "../views/tests/GetStarted.vue";
import Datenschutz from "../views/general/Datenschutz.vue";
import Profile from "../views/profile/ProfileLanding.vue";
import TestLanding from "../views/tests/TestLanding.vue";
import TrainingsLanding from "../views/trainings/TrainingsLanding.vue";
import Dashboard from "../views/report/Dashboard.vue";
import PathNotFound from "../views/general/PathNotFound.vue";
import Test from "../views/tests/Test.vue";
import TestIntroduction from "../views/tests/TestIntroduction.vue";
import Login from "../views/self-service/Login.vue";
import SessionExpired from "../views/self-service/SessionExpired.vue";
import SelfServicePortal from "../views/self-service/SelfServicePortal.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },

  {
    path: "/getstarted",
    name: "GetStarted",
    component: GetStarted,
    meta: { getStartedActive: true },
  },

  {
    path: "/competence-tests/introduction/:invitationToken?",
    name: "TestIntroduction",
    component: TestIntroduction,
    meta: { invitationToken: true, testButtonActive: true }, // This meta field will be used to check for invitation token
  },
  {
    path: "/competence-tests/profile/:invitationToken?",
    name: "Profile",
    component: Profile,
    meta: { testButtonActive: true },
  },
  {
    path: "/competence-tests/overview/:invitationToken?",
    name: "TestLanding",
    component: TestLanding,
    meta: { invitationToken: true, testButtonActive: true },
  },
  {
    path: "/dashboard",
    name: "SelfServicePortal",
    component: SelfServicePortal,
    meta: { requiresAuth: true }, 
  },
  {
    path: "/competence-tests/test/:invitationToken?",
    name: "Test",
    component: Test,
    meta: { invitationToken: true, testButtonActive: true }, 
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: {
      guestOnly: true,
    },
  },
  {
    path: "/login/expired",
    name: "SessionExpired",
    component: SessionExpired,
  },
  {
    path: "/competence-tests/dashboard/",
    name: "Dashboard",
    component: Dashboard,
    meta: { testButtonActive: true },

  },
  
  {
    path: "/account",
    name: "Account",
    component: Login,
  },
  {
    path: "/datenschutz",
    name: "Datenschutz",
    component: Datenschutz,
  },
  {
    path: "/competence-tests/trainings/",
    name: "TrainingsLanding",
    component: TrainingsLanding,
    meta: { testButtonActive: true },

  },
  { path: "/:pathMatch(.*)*", component: PathNotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 };
  },
});

router.beforeEach(async (to, from, next) => {
  const auth = useAuthStore();

  const campagneStore = useCampagneStore();

  // Wait for the app's authentication status check to complete
  if (auth.isInitializing && auth.authPromise) {
    await auth.authPromise;
  }
  const isInvitationTokenRote = to.matched.some(
    (record) => record.meta.invitationToken
  );

  if (isInvitationTokenRote) {
    const token = to.params.invitationToken;

    if (token) {
      let validToken = false;
      validToken = await campagneStore.validateInvitationToken(token);

      if (validToken) {
        return next();
      } else {
        return next({ path: "/getstarted", query: { redirect: to.fullPath } });
      }
    }
  }

  const isProtectedRoute = to.matched.some(
    (record) => record.meta.requiresAuth
  );

  // If user is trying to access the /login route while already logged in, redirect to dashboard
  if (to.path === "/login" && auth.isLoggedIn) {
    next("/dashboard"); 
    return;
  }

  // For accessing protected routes
  if (isProtectedRoute && !auth.isLoggedIn) {
    return next({ path: "/login", query: { redirect: to.fullPath } });
  } else {
    return next();
  }
});

export default router;

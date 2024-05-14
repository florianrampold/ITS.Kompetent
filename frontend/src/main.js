import { createApp } from "vue";
import { createPinia } from "pinia";
import { backendURL } from '@/config.js'; // Make sure the path is correct based on your file structure
//import { useCompetenceTestStore } from "@/stores/CompetenceTestStore";
import App from "./App.vue";
import "./styles/app.css";
import router from "./router";
import APIService from "./services/api.service.js";
import Spinner from "@/components/base/Spinner.vue";
import PopUp from "@/components/base/PopUp.vue";
import SkeletonLoader from "@/components/base/Skeleton.vue";

import {
  LockClosedIcon,
  CloudArrowUpIcon,
  CloudArrowDownIcon,
  TrashIcon,
  DocumentDuplicateIcon,
  DocumentArrowDownIcon,
  ArrowPathIcon,
  KeyIcon,
  XMarkIcon,
  XCircleIcon,
  ExclamationTriangleIcon,
  InformationCircleIcon,
  CheckIcon,
  ChevronDownIcon,
  CheckCircleIcon,
  MegaphoneIcon,
  ArrowLeftEndOnRectangleIcon,
  ArrowTrendingUpIcon,
  IdentificationIcon,
  ChartBarIcon,
  UsersIcon,
  ChevronUpDownIcon,
  Bars3BottomRightIcon,
} from "@heroicons/vue/20/solid";

//const useStore = useCompetenceTestStore();
const pinia = createPinia();

const app = createApp(App);
APIService.init(backendURL);
APIService.setHeader();
app.use(pinia);
app.use(router);

app.component("Spinner", Spinner);
app.component("SkeletonLoader", SkeletonLoader);

app.component("PopUp", PopUp);
app.component("LockClosedIcon", LockClosedIcon);
app.component("CloudArrowUpIcon", CloudArrowUpIcon);
app.component("ChevronDownIcon", ChevronDownIcon);
app.component("ChevronUpDownIcon", ChevronUpDownIcon);
app.component("Bars3BottomRightIcon", Bars3BottomRightIcon);

app.component("CloudArrowDownIcon", CloudArrowDownIcon);
app.component("TrashIcon", TrashIcon);
app.component("DocumentDuplicateIcon", DocumentDuplicateIcon);
app.component("DocumentArrowDownIcon", DocumentArrowDownIcon);
app.component("ArrowPathIcon", ArrowPathIcon);
app.component("ArrowTrendingUpIcon", ArrowTrendingUpIcon);
app.component("IdentificationIcon", IdentificationIcon);
app.component("ChartBarIcon", ChartBarIcon);
app.component("UsersIcon", UsersIcon);

app.component("ArrowLeftEndOnRectangleIcon", ArrowLeftEndOnRectangleIcon);

app.component("KeyIcon", KeyIcon);
app.component("MegaphoneIcon", MegaphoneIcon);
app.component("XMarkIcon", XMarkIcon);
app.component("CheckIcon", CheckIcon);
app.component("XCircleIcon", XCircleIcon);
app.component("CheckCircleIcon", CheckCircleIcon);
app.component("ExclamationTriangleIcon", ExclamationTriangleIcon);
app.component("InformationCircleIcon", InformationCircleIcon);

app.mount("#app");
//createApp(App).use(router).mount("#app");

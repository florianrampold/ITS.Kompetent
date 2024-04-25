/* eslint-disable */
<template>
  <div class="overflow-x-auto">
    <div class="flex min-w-max h-256 flex-col mb-10">
      <div class="flex flex-1 overflow-hidden">
        <div
          class="p-6 w-24 bg-white rounded-l-lg overflow-y-auto overflow-x-auto"
        >
          <nav>
            <!-- <h2
            class="text-gray-600 text-xs font-semibold uppercase tracking-wider"
          >
            Postfach
          </h2> -->
            <div class="mt-4">
              <a
                class="-mx-4 px-3 py-1 flex items-center justify-between text-sm font-medium bg-gray-100 rounded-lg"
              >
                <span class="inline-flex">
                  <InboxIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></InboxIcon>
                  <!-- <span class="ml-2 text-gray-900">Posteingang</span> -->
                </span>
                <!-- <span
                class="px-4 py-1 inline-block leading-tight text-xs font-semibold text-gray-900 bg-green-200 rounded-full"
                >{{ emails.length }}</span
              > -->
              </a>
            </div>
            <div class="mt-4">
              <a
                class="-mx-4 px-3 py-1 flex items-center justify-between text-sm font-medium bg-gray-100 rounded-lg"
              >
                <span class="inline-flex">
                  <ChevronDoubleRightIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></ChevronDoubleRightIcon>
                  <!-- <span class="ml-2 text-gray-900">Gesendet</span> -->
                </span>
              </a>
            </div>
            <div class="mt-4">
              <a
                class="-mx-4 px-3 py-1 flex items-center justify-between text-sm font-medium bg-gray-100 rounded-lg"
              >
                <span class="inline-flex">
                  <TrashIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></TrashIcon>
                  <!-- <span class="ml-2 text-gray-900">Papierkorb</span> -->
                </span>
              </a>
            </div>
          </nav>
        </div>

        <main class="flex flex-1 bg-white rounded-r-lg">
          <div class="flex flex-col w-full max-w-xs border-l border-r">
            <div
              class="flex flex-shrink-0 items-center justify-between border-b"
            >
              <button
                class="px-4 py-2 flex items-center text-xs font-semibold text-gray-600"
              >
                Sortieren nach Datum
              </button>
              <button class="pr-2">
                <BarsArrowDownIcon
                  class="fill-current text-gray-700 w-6 h-6"
                ></BarsArrowDownIcon>
              </button>
            </div>
            <div class="flex-1 overflow-y-auto overflow-x-auto text-left">
              <div v-if="filterIndex == -1">
                <div v-for="(email, key) in emailImpulseItems" :key="key">
                  <a
                    class="block px-6 pt-3 pb-4 bg-gray-100 border-b-2 cursor-pointer"
                    @click="getActiveEmail(email)"
                  >
                    <span
                      class="text-md font-bold text-gray-900 pb-10 text-left"
                    >
                      Szenario {{ key + 1 }}
                    </span>
                    <div class="flex justify-between mt-5">
                      <span
                        class="text-sm font-semibold text-gray-900 text-left"
                      >
                        {{ email.email_sender }}
                      </span>
                      <span class="text-sm text-gray-600 text-right">
                        {{ email.email_date }}
                      </span>
                    </div>
                    <p class="flex mt-2 justify-start text-sm text-gray-900">
                      {{ email.email_regarding }}
                    </p>
                    <p
                      class="flex justify-start mt-2 text-sm text gray-600 whitespace-pre-line"
                    >
                      {{ email.email_teaser }}
                    </p>
                  </a>
                </div>
              </div>
              <div v-else>
                <div v-for="email in emailImpulseItems" :key="email">
                  <a
                    class="block px-6 pt-3 pb-4 bg-gray-100 border-b-2 cursor-pointer"
                    @click="getActiveEmail(email)"
                  >
                    <span
                      class="text-md font-bold text-gray-900 pb-10 text-left"
                    >
                      Szenario {{ currentIndex }}
                    </span>
                    <div class="flex justify-between mt-5">
                      <span
                        class="text-sm font-semibold text-gray-900 text-left"
                      >
                        {{ email.email_sender }}
                      </span>
                      <span class="text-sm text-gray-600 text-right">
                        {{ email.email_date }}
                      </span>
                    </div>
                    <p class="flex mt-2 justify-start text-sm text-gray-900">
                      {{ email.email_regarding }}
                    </p>
                    <p
                      class="flex justify-start mt-2 text-sm text gray-600 whitespace-pre-line"
                    >
                      {{ email.email_teaser }}
                    </p>
                  </a>
                </div>
              </div>
            </div>
          </div>

          <div class="flex-1">
            <div class="h-20 p-5 border-b">
              <div class="flex items-center">
                <span class="">
                  <BackspaceIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></BackspaceIcon>
                </span>
                <span class="ml-6">
                  <ArrowUturnLeftIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></ArrowUturnLeftIcon>
                </span>
                <span class="ml-6">
                  <ArrowRightCircleIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></ArrowRightCircleIcon>
                </span>
                <span class="ml-6">
                  <TrashIcon
                    class="fill-current text-gray-700 w-6 h-6"
                  ></TrashIcon>
                </span>
              </div>
            </div>
            <div
              class="flex items-center justify-between px-5 py-4 bg-gray-100 border-r"
            >
              <h3 class="text-xl text-gray-900 text-left">
                {{ activeEmail.email_regarding }}
              </h3>
              <h3 class="text-sm text-gray-900 text-right">
                {{ activeEmail.email_date }}
              </h3>
            </div>
            <div
              class="flex items-center justify-start px-5 py-4 bg-gray-100 border-r"
            >
              <!-- <img
              class="h-12 w-12 rounded-full object-cover"
              src="@/assets/email_picture.jpg"
              alt=""
            /> -->
              <div class="flex flex-col px-8">
                <h3 class="text-lg flex justfy-start text-gray-900">
                  {{ activeEmail.email_sender }}
                </h3>
                <h3 class="text-lg flex justfy-start text-gray-900">
                  <span class="font-semibold">An:&nbsp;</span>
                  {{ activeEmail.email_recipient }}
                </h3>
              </div>
            </div>
            <div
              v-if="activeEmail.email_content"
              class="p-3 m-6 flex flex-row w-220 bg-gray-100 flex justify-start rounded-lg text-left"
            >
              <!-- eslint-disable-next-line vue/no-v-html -->
              <div
                class="flex flex-col"
                :class="{ 'w-2/5': activeEmail.email_is_signed_image }"
              >
                <article
                  class="whitespace-pre-line"
                  style="word-wrap: break-word whitespace-pre-line overflow-wrap: break-word"
                  v-html="safeHtml"
                ></article>
              </div>
              <div
                v-if="activeEmail.email_is_signed_image"
                class="w-3/5 flex items-center justify-center p-5"
              >
                <img
                  class="h-auto"
                  :src="activeEmail.email_is_signed_image"
                  alt="Email Attachment"
                />
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>

<script>
import { InboxIcon } from "@heroicons/vue/20/solid";
import { BackspaceIcon } from "@heroicons/vue/20/solid";
import { ArrowUturnLeftIcon } from "@heroicons/vue/20/solid";
import { ArrowRightCircleIcon } from "@heroicons/vue/20/solid";
import { TrashIcon } from "@heroicons/vue/20/solid";
import { BarsArrowDownIcon } from "@heroicons/vue/20/solid";
import { ChevronDoubleRightIcon } from "@heroicons/vue/20/solid";
import DOMPurify from "dompurify";
export default {
  components: {
    BackspaceIcon,
    InboxIcon,
    ArrowUturnLeftIcon,
    ArrowRightCircleIcon,
    TrashIcon,
    BarsArrowDownIcon,
    ChevronDoubleRightIcon,
  },
  props: {
    emails: {
      type: Array,
      default: null,
    },
    filterIndex: {
      type: Number,
      default: -1,
    },
  },
  data() {
    return {
      activeEmail: "",
      emailImpulseItems: [],
      currentIndex: 1,
    };
  },
  computed: {
    safeHtml() {
      return DOMPurify.sanitize(this.activeEmail.email_content);
    },
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * If filterIndex is not -1 (Threat Awareness) shoe the email which is the most threatining.
   */
  mounted() {
    this.emailImpulseItems = this.emails;
    if (this.filterIndex != -1) {
      this.emailImpulseItems = [];
      this.emailImpulseItems[0] = this.emails[this.filterIndex];
      this.currentIndex = this.filterIndex + 1;
    }
    this.activeEmail = this.emailImpulseItems[0];
  },

  methods: {
    /**
     * Gets and changes the active e-mail.
     */
    getActiveEmail(email) {
      this.activeEmail = email;
    },
  },
};
</script>

<style scoped></style>

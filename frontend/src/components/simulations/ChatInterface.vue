<template>
  <div class="bg-white rounded shadow-2xl">
    <nav
      class="w-full h-14 bg-gray-600 rounded-tr rounded-tl flex justify-between items-center"
    >
      <div class="flex justify-center items-center">
        <i class="mdi mdi-arrow-left font-normal text-gray-300 ml-1"></i>
        <img
          v-if="chat.chat_sender_image"
          :src="chat.chat_sender_image"
          class="rounded-full ml-1 w-10 h-10"
        />
        <span class="text-lg font-medium text-gray-300 ml-1">{{
          chat.chat_sender_name
        }}</span>
      </div>

      <div class="flex items-center">
        <VideoCameraIcon class="w-8 h-8 text-white mr-4"></VideoCameraIcon>
        <PhoneIcon class="w-8 h-8 text-white mr-4"></PhoneIcon>
        <Bars3BottomLeftIcon
          class="w-8 h-8 mr-2 text-white"
        ></Bars3BottomLeftIcon>
      </div>
    </nav>

    <div
      id="journal-scroll"
      class="overflow-auto px-1 py-1"
      style="height: 19rem"
    >
      <div class="flex flex-col items-center pr-10">
        <div class="flex mt-5 ml-1 py-2 px-4 rounded-lg bg-gray-100 text-left">
          Heute
        </div>
        <div
          class="flex mt-5 ml-1 py-2 px-4 rounded-lg bg-yellow-100 text-left"
        >
          Nachrichten und Anrufe sind Ende-zu-Ende-verschlüsselt. Niemand
          außerhalb des Chats kann sie lesen oder anhören.
        </div>
        <div
          class="flex mt-5 ml-1 py-2 px-4 rounded-lg bg-gray-100 text-center text-uppercase"
        >
          1 Ungelesene Nachricht
        </div>
        <div
          class="flex ml-1 h-auto bg-gray-200 text-gray-200 text-md font-normal rounded-lg text-left my-4 px-4 p-1 items-end"
          style="font-size: 20px"
        >
          <span class="text-black whitespace-pre-line">
            {{ chat.chat_message_incoming }}
          </span>
          <span class="text-gray-600 pl-1" style="font-size: 14px">15:38</span>
        </div>
      </div>
      <div
        v-if="!chat.chat_sender_known"
        class="w-full mt-5 ml-1 py-2 px-4 bg-gray-100"
      >
        Dieser Absender ist nicht in deinen Kontakten
      </div>

      <div class="flex justify-end pt-2 pl-10">
        <span
          v-if="chat.chat_message_outgoing"
          class="bg-green-900 h-auto text-gray-200 text-md font-normal rounded-lg px-1 p-1 items-end flex justify-end"
          style="font-size: 20px"
          >{{ chat.chat_message_outgoing }}
          <span class="text-gray-400 pl-1" style="font-size: 14px">{{
            chat.chat_message_outgoing_date
          }}</span></span
        >
      </div>

      <div
        v-if="chat.chat_message_incoming_2"
        class="flex items-center pr-10 mt-1"
      >
        <img
          src="https://i.imgur.com/IAgGUYF.jpg"
          class="rounded-full shadow-xl"
          width="25"
          height="25"
        />
        <span
          class="flex ml-1 h-auto bg-gray-600 text-gray-200 text-md p-1 font-normal rounded-lg px-1 items-end"
          style="font-size: 20px"
          >{{ chat.chat_message_incoming_2 }}
          <span class="text-gray-400 pl-1" style="font-size: 14px"
            >01:25am</span
          ></span
        >
      </div>

      <div id="chatmsg" class=" "></div>
    </div>

    <div class="flex justify-between p-1">
      <div class="w-5/6 relative">
        <FaceSmileIcon
          class="w-8 h-8 absolute top-1 left-1 text-white"
        ></FaceSmileIcon>

        <input
          id="typemsg"
          type="text"
          class="rounded-full w-full pl-12 pr-12 py-2 focus:outline-none h-auto placeholder-gray-100 bg-gray-600 text-white"
          style="font-size: 16px"
          placeholder="Nachricht.."
        />
        <PaperClipIcon
          class="w-8 h-8 hidden sm:block absolute right-12 top-1 text-white"
        ></PaperClipIcon>

        <CameraIcon
          class="w-8 h-8 hidden sm:block absolute right-2 top-1 text-white"
        ></CameraIcon>
      </div>

      <div class="flex">
        <div
          class="w-10 h-10 mx-4 rounded-full bg-blue-300 text-center items-center flex justify-center hover:bg-blue-600 hover:text-white"
        >
          <MicrophoneIcon class="w-8 h-8 text-white"></MicrophoneIcon>
        </div>
        <div
          class="w-10 h-10 mr-1 rounded-full bg-blue-300 text-center items-center hover:bg-blue-600 flex justify-center"
        >
          <PlayIcon class="w-8 h-8 text-white"></PlayIcon>
        </div>
      </div>
    </div>
  </div>
  <div
    class="flex w-full h-14 bg-gray-600 rounded-b text-white text-lg font-medium items-center justify-center text-center"
  >
    <span class=""> Szenario {{ currentIndex }} </span>
  </div>
</template>
<script>
import { CameraIcon } from "@heroicons/vue/20/solid";
import { VideoCameraIcon } from "@heroicons/vue/20/solid";

import { PhoneIcon } from "@heroicons/vue/20/solid";
import { Bars3BottomLeftIcon } from "@heroicons/vue/20/solid";
import { PaperClipIcon } from "@heroicons/vue/20/solid";
import { FaceSmileIcon } from "@heroicons/vue/20/solid";
import { PlayIcon } from "@heroicons/vue/20/solid";
import { MicrophoneIcon } from "@heroicons/vue/20/solid";

export default {
  components: {
    CameraIcon,
    PhoneIcon,
    Bars3BottomLeftIcon,
    PaperClipIcon,
    FaceSmileIcon,
    PlayIcon,
    VideoCameraIcon,
    MicrophoneIcon,
  },
  props: {
    chat: {
      type: Object,
      default: null,
    },
    currentIndex: {
      type: Number,
      default: 0,
    },
  },
};
</script>

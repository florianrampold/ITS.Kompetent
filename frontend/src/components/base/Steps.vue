<template>
  <section>
    <!-- component -->
    <div class="">
      <div id="ProgressStepper" class="flex">
        <!-- progress item -->
        <div class="w-1/4">
          <div class="relative mb-2">
            <div
              :class="{
                'bg-green-500 border-2 border-action': activestate == '1',
              }"
              class="w-10 h-10 mx-auto bg-gray-400 cursor-pointer rounded-full text-lg text-white flex items-center"
              @click="changeStep(1)"
            >
              <span class="text-center text-white font-bold w-full"> 1 </span>
            </div>
          </div>

          <h3
            class="text-xs invisible sm:visible sm:text-md lg:text-lg lg:text-xl font-bold text-center"
          >
            ITS-Anforderungsprofil
          </h3>
        </div>
        <!-- /progress item -->

        <!-- progress item middle -->
        <div class="w-1/4">
          <div class="relative mb-2">
            <div
              class="absolute flex align-center items-center align-middle content-center"
              style="
                width: calc(100% - 2.5rem - 1rem);
                top: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <div
                :class="[`bg-${linecolor}-200`]"
                class="w-full bg-white rounded items-center align-middle align-center flex-1"
              >
                <div
                  class="w-0 bg-green-300 py-1 rounded"
                  style="width: ${procentBar}%;"
                ></div>
                <!-- middle part 100 full & 50 half progressstatus-->
              </div>
            </div>

            <div
              :class="{ 'bg-action': activestate == '2' }"
              class="w-10 h-10 mx-auto bg-gray-400 cursor-pointer hover:bg-green-500 rounded-full text-lg text-white flex items-center"
              @click="changeStep(2)"
            >
              <span class="text-center text-white font-bold w-full"> 2 </span>
            </div>
          </div>

          <div
            class="text-xs invisible sm:visible sm:text-md lg:text-xl font-bold text-center"
          >
            ITS-Kompetenzen
          </div>
        </div>
        <!-- progress item middle -->
        <div class="w-1/4">
          <div class="relative mb-2">
            <div
              class="absolute flex align-center items-center align-middle content-center"
              style="
                width: calc(100% - 2.5rem - 1rem);
                top: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <div
                :class="[`bg-${linecolor}-200`]"
                class="w-full bg-white rounded items-center align-middle align-center flex-1"
              >
                <div
                  class="w-0 bg-green-300 py-1 rounded"
                  style="width: ${procentBar}%;"
                ></div>
                <!-- middle part 100 full & 50 half progressstatus-->
              </div>
            </div>

            <div
              :class="{ 'bg-action': activestate == '3' }"
              class="w-10 h-10 mx-auto bg-gray-400 cursor-pointer hover:bg-green-500 rounded-full text-lg text-white flex items-center"
              @click="changeStep(3)"
            >
              <span class="text-center text-white font-bold w-full"> 3 </span>
            </div>
          </div>

          <div
            class="text-xs invisible sm:visible sm:text-md lg:text-xl font-bold text-center"
          >
            Statistiken
          </div>
        </div>

        <!-- progress item middle -->
        <div class="w-1/4">
          <div class="relative mb-2">
            <div
              class="absolute flex align-center items-center align-middle content-center"
              style="
                width: calc(100% - 2.5rem - 1rem);
                top: 50%;
                transform: translate(-50%, -50%);
              "
            >
              <div
                :class="[`bg-${linecolor}-200`]"
                class="w-full bg-white rounded items-center align-middle align-center flex-1"
              >
                <div
                  class="w-0 bg-green-300 py-1 rounded"
                  style="width: ${procentBar}%;"
                ></div>
                <!-- middle part 100 full & 50 half progressstatus-->
              </div>
            </div>

            <div
              :class="{ 'bg-action': activestate == '4' }"
              class="w-10 h-10 mx-auto bg-gray-400 hover:bg-green-500 cursor-pointer rounded-full text-lg text-white flex items-center"
              @click="changeStep(4)"
            >
              <span class="text-center text-white font-bold w-full"> 4 </span>
            </div>
          </div>

          <div
            class="text-xs invisible sm:visible sm:text-md lg:text-xl font-bold text-center"
          >
            ITS-Trainingsempfehlungen
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    linecolor: {
      type: String,
      default: "gray",
    },
    activestate: {
      type: Number,
      default: 0,
    },
    choosingMode: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["changeStep"],
  mounted() {},
  methods: {
    /**
     * Changes the active step when choosingMode is true defined in the parent component.
     * Emits the active step to the parent component.
     *
     */
    changeStep(activestate) {
      if (this.choosingMode) {
        this.$emit("changeStep", activestate);
      }
    },
  },
};
</script>

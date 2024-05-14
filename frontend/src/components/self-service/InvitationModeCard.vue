<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="bg-white border-2 h-300 xl:h-200 border-white rounded-lg">
    <div class="mx-auto px-4 sm:px-6 lg:px-8">
      <div
        class="mt-8 space-y-4 sm:space-y-0 lg:max-w-4xl lg:mx-auto xl:max-w-none xl:mx-0 xl:grid-cols-2"
      >
        <div class="p-6">
          <h2 class="text-xl leading-6 font-medium text-gray-900">
            {{ name }}
          </h2>
          <p class="mt-4 text-lg whitespace-pre-line text-gray-500">
            {{ description }}
          </p>
        </div>
        <div class="w-full rounded-md shadow">
          <button
            class="w-full flex items-center justify-center px-8 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primaryAccent py-2 md:text-lg md:px-10"
            @click="selectCard(id)"
          >
            Auswählen und Weiter
          </button>
        </div>
        <div class="pt-10 pb-8 px-6">
          <h3
            class="text-lg font-medium divide-y divide-gray-200 text-gray-900 tracking-wide uppercase"
          >
            Übersicht
          </h3>
          <ul role="list" class="mt-6 space-y-4">
            <li
              v-for="(benefit, index) in benefits"
              :key="benefit"
              class="flex space-x-3"
            >
              <CheckIcon
                class="flex-shrink-0 h-5 w-5 text-green-500"
                aria-hidden="true"
              />

              <span class="text-sm md:text-lg text-gray-500">{{
                benefit.text
              }}</span>
              <ToolTip
                :is-visible="showBenefits[index]"
                @update-is-visible="(val) => (showBenefits[index] = val)"
              >
                <template #trigger>
                  <!-- Use InformationCircleIcon as a trigger -->
                  <InformationCircleIcon
                    class="h-4 w-4 text-gray-400 hover:text-gray-500"
                    @mouseenter="showBenefits[index] = true"
                    @mouseleave="showBenefits[index] = false"
                  />
                </template>
                {{ benefit.toolTipText }}
              </ToolTip>
            </li>
          </ul>
          <ul role="list" class="mt-6 space-y-4">
            <li
              v-for="(disadvantage, index) in disadvantages"
              :key="disadvantage"
              class="flex space-x-3"
            >
              <XMarkIcon
                class="flex-shrink-0 h-5 w-5 text-red-500"
                aria-hidden="true"
              />

              <span class="text-sm md:text-lg text-gray-500">{{
                disadvantage.text
              }}</span>
              <ToolTip
                :is-visible="showDisadvantages[index]"
                @update-is-visible="(val) => (showDisadvantages[index] = val)"
              >
                <template #trigger>
                  <!-- Use InformationCircleIcon as a trigger -->
                  <InformationCircleIcon
                    class="h-4 w-4 text-gray-400 hover:text-gray-500"
                    @mouseenter="showDisadvantages[index] = true"
                    @mouseleave="showDisadvantages[index] = false"
                  />
                </template>
                {{ disadvantage.toolTipText }}
              </ToolTip>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ToolTip from "@/components/base/ToolTip";

export default {
  components: {
    ToolTip,
  },
  props: {
    name: {
      type: String,
      default: "",
    },
    description: {
      type: String,
      default: "",
    },
    toolTipText: {
      type: String,
      default: "",
    },
    benefits: {
      type: Array,
      default: () => [],
    },
    disadvantages: {
      type: Array,
      default: () => [],
    },
    label: {
      type: Number,
      default: 0,
    },
    value: {
      type: Number,
      default: 0,
    },
    id: {
      type: Number,
      default: 0,
    },
  },
  emits: ["change"],
  data() {
    return {
      showBenefits: {}, // Object to track visibility of tooltips, indexed by benefit index
      showDisadvantages: {}, // Object to track visibility of tooltips, indexed by benefit index
    };
  },

  methods: {
    /**
     * Changes the selection of the invitation mode card and emits the event to the parent component.
     * @param {Number} id The ID of the invitation mode card.
     */
    selectCard(id) {
      this.$emit("change", id);
    },
  },
};
</script>

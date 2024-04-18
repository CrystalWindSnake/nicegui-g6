<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Graph, GraphData, TreeGraphData, type GraphOptions } from "@antv/g6";
import { getExtractEventObjectFn } from "./core";

type TData = GraphData | TreeGraphData | undefined;

// props
const props = defineProps<{
  data: TData;
  graphOptions: GraphOptions;
  resource_path: String;
}>();

// emits
const emits = defineEmits<{
  (event: "graph-event", params: { eventName: string; data: any }): void;
}>();

// expose
defineExpose({
  onEvent: (eventName: string, args: string[] | string) => {
    console.log("onEvent", eventName, args);

    let argsMapFn = getExtractEventObjectFn(args);

    if (graph) {
      graph.on(eventName, (ev) => {
        const extractedValues = argsMapFn(ev);

        console.log("graph event", eventName, extractedValues);
        emits("graph-event", { eventName, data: extractedValues });
      });
    }
  },
});

// main
const containerRef = ref<HTMLDivElement>();
let graph: Graph | undefined;

onMounted(async () => {
  if (!containerRef.value) {
    return;
  }

  const container = containerRef.value;

  const width = container.clientWidth;
  const height = container.clientHeight;

  graph = new Graph({
    ...props.graphOptions,
    container,
    width,
    height,
  });

  graph.data(props.data);

  graph.render(); // 渲染图
});
</script>

<template>
  <div ref="containerRef" class="nicegui-g6-container"></div>
</template>

<style scoped>
:where(.nicegui-g6-container) {
  width: 100%;
  min-height: 16rem;
}
</style>

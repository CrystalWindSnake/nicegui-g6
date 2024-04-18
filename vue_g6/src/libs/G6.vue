<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Graph, GraphData, TreeGraphData, type GraphOptions } from "@antv/g6";

type TData = GraphData | TreeGraphData | undefined;

const props = defineProps<{
  data: TData;
  graphOptions: GraphOptions;
  resource_path: String;
}>();

const containerRef = ref<HTMLDivElement>();

onMounted(async () => {
  if (!containerRef.value) {
    return;
  }

  const container = containerRef.value;

  const width = container.clientWidth;
  const height = container.clientHeight;

  const graph = new Graph({
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

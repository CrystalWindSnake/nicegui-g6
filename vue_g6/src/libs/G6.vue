<script setup lang="ts">
import { onMounted, ref } from "vue";
import { Graph } from "@antv/g6";
// const props = defineProps<{ component: TComponent }>()

const containerRef = ref<HTMLDivElement>();

const data = {
  // 点集
  nodes: [
    {
      type: "modelRect",
      id: "node1",
      label: "test label1",
    },
    {
      type: "modelRect",
      id: "node2",
      label: "test label2",
    },
    {
      type: "modelRect",
      id: "node3",
      label: "test label3",
    },

    {
      type: "modelRect",
      id: "node4",
      label: "test label4",
    },
  ],
  // 边集
  edges: [
    {
      source: "node1",
      target: "node2",
    },
    {
      source: "node1",
      target: "node3",
    },

    {
      source: "node2",
      target: "node4",
    },
    {
      source: "node3",
      target: "node4",
    },
  ],
};

onMounted(() => {
  if (!containerRef.value) {
    return;
  }

  const container = containerRef.value;

  const width = container.clientWidth;
  const height = container.clientHeight;

  const graph = new Graph({
    container, // String | HTMLElement，必须，在 Step 1 中创建的容器 id 或容器本身
    width, // Number，必须，图的宽度
    height, // Number，必须，图的高度
    // fitCenter: true, // Boolean，可选，图是否自适应中心位置
    modes: {
      default: ["drag-canvas", "drag-node", "zoom-canvas"], // 允许的操作
    },
    layout: {
      type: "dagre",
      rankdir: "LR", // 图的方向，TB 为从上到下，BT 为从下到上，RL 为从右到左，LR 为从左到右
    },
    fitView: true, // Boolean，可选，图是否自适应视野,
    defaultNode: {
      size: [200, 80],
      type: "modelRect", // 节点类型
      style: {
        fill: "#f0f5ff",
        stroke: "#adc6ff",
        lineWidth: 2,
      },
    },
    defaultEdge: {
      type: "polyline",
      size: 1,
      color: "#e2e2e2",
      style: {
        endArrow: {
          path: "M 0,0 L 8,4 L 8,-4 Z",
          fill: "#e2e2e2",
        },
        radius: 20,
      },
    },
    // 节点不同状态下的样式集合
    nodeStateStyles: {
      // 鼠标 hover 上节点，即 hover 状态为 true 时的样式
      hover: {
        fill: "red",
      },
      // 鼠标点击节点，即 click 状态为 true 时的样式
      click: {
        stroke: "#000",
        lineWidth: 3,
      },
    },
  });

  graph.data(data); // 读取 Step 2 中的数据源到图上

  // 鼠标进入节点
  graph.on("node:mouseenter", (e) => {
    const nodeItem = e.item; // 获取鼠标进入的节点元素对象
    graph.setItemState(nodeItem, "hover", true); // 设置当前节点的 hover 状态为 true
  });

  // 鼠标离开节点
  graph.on("node:mouseleave", (e) => {
    const nodeItem = e.item; // 获取鼠标离开的节点元素对象
    graph.setItemState(nodeItem, "hover", false); // 设置当前节点的 hover 状态为 false
  });

  // 点击节点
  graph.on("node:click", (e) => {
    // 先将所有当前是 click 状态的节点置为非 click 状态
    const clickNodes = graph.findAllByState("node", "click");
    clickNodes.forEach((cn) => {
      graph.setItemState(cn, "click", false);
    });
    const nodeItem = e.item; // 获取被点击的节点元素对象
    graph.setItemState(nodeItem, "click", true); // 设置当前节点的 click 状态为 true
  });

  graph.render(); // 渲染图
});
</script>

<template>
  <div
    ref="containerRef"
    style="height: 50vh; width: 50vw; border: 1px solid #000"
  ></div>
</template>

<style scoped></style>

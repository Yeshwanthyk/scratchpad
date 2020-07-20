<template>
  <div class="place">
    <img :src="location.img" width="235" height="300" />
    <slot></slot>
    <p>{{ location.desc }}</p>
  </div>
</template>

<script>
export default {
  props: ["location"]
};
</script>

<style lang="scss" scoped>
</style>
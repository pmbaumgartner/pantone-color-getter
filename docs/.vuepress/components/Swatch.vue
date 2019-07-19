<template>
  <td :style="style">
    <strong>{{text}}</strong>
  </td>
</template>

<script>
module.exports = {
  props: {
    bgcolor: { required: true },
    fc: { required: true },
    text: { required: true }
  },
  computed: {
    style() {
      return { color: this.fc, backgroundColor: this.bgcolor };
    }
  }
};
</script>

<style scoped>
</style>
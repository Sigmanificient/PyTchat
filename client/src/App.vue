<template>
	<router-view :key="$route.path" />
</template>
<script>
export default {
	name: "App",
};
</script>
<style>
body {
	margin: 0;
}
</style>

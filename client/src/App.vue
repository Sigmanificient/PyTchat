<template>
	<router-view :key="$route.path"/>
</template>
<script>
export default {
	name: "App",
};
</script>
<style>
body {
	color: #8dbeba;
	font-family: 'Poppins', sans-serif;
	margin: 0;
}
</style>

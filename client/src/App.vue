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
	background-color: #0e1018;
	font-size: clamp(10px, 1.5vw, 16px);
	font-family: 'Poppins', sans-serif;
	margin: 0;
}
</style>

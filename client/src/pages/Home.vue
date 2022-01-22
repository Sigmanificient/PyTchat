<template>
	<div class="login_fom">
		<div class="form-group">
			<label>Server IP Address</label>
			<input v-model="address" placeholder="127.0.0.1">
		</div>
		<div class="form-group">
			<label>Server Port</label>
			<input type="number" v-model.number="port" placeholder="4269">
		</div>
		<br>
		<div class="form-group">
			<label>Username</label>
			<input v-model="username" placeholder="Boop">
		</div>
		<div class="form-group">
			<input type="submit">
		</div>
	</div>
</template>

<script>
export default {
	name: "Home",
	data() {
		return {
			address: "",
			port: 0,
			username: ""
		};
	}
}
</script>
<style scoped>

</style>
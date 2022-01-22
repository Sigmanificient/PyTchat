<template>
	<main class="from_wrapper">
		<div class="login_fom">
			<div class="server-info">
				<div class="form-group">
					<label>Server IP Address</label>
					<input v-model="address" placeholder="127.0.0.1">
				</div>
				<div class="form-group">
					<label>Server Port</label>
					<input type="number" v-model.number="port" placeholder="4269">
				</div>
			</div>

			<div class="form-group">
				<label>Username</label>
				<input v-model="username" placeholder="Boop">
			</div>

			<div class="form-group">
				<input @click="login()" type="submit">
			</div>
		</div>
	</main>
</template>

<script>
export default {
	name: "Home",
	data() {
		return {
			address: "",
			port: null,
			username: ""
		};
	},
	methods: {
		login() {
			this.$router.push({
				name: "tchat",
				params: {
					address: this.address,
					port: this.port,
					username: this.username
				}
			});
		}
	}
}
</script>
<style scoped>
.from_wrapper {
	display: grid;
	place-items: center;
	height: 100vh;
}

.server-info {
	display: flex;
	gap: 2em;
}

.login_fom {
	display: grid;
	grid-gap: 2em;
	background-color: #131926;
	padding: 2em;
}

.form-group {
	display: flex;
	flex-direction: column;
	gap: 0.5em;
}

.form-group label {
	font-size: 0.8em;
}

.form-group input {
	border: none;
	border-bottom: 1px solid #1e3348;
	background-color: transparent;
	color: inherit;
	padding: 0.5em;
}

.form-group input[type=number] {
	-webkit-appearance: none;
	-moz-appearance: textfield;
	margin: 0;
}

.form-group input[type=submit] {
	border: none;
	background-color: #1e3348;
	font-size: 1em;
	padding: 0.5em 2em;
	cursor: pointer;
	width: fit-content;
}

@media (max-width: 540px) {
	.server-info {
		flex-direction: column;
	}
}
</style>
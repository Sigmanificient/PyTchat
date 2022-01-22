<template>
	<header class="header">
		<h1>Tchat</h1>
		<p>Connected as {{ username }}</p>
	</header>
</template>

<script>
export default {
	name: "Tchat",
	data() {
		return {
			address: this.$route.params.address,
			port: this.$route.params.port,
			username: this.$route.params.username,
		}
	},
	mounted() {
		let ws = new WebSocket(`ws://${this.address}:${this.port}`);
		ws.onopen = () => {
			ws.send(
				JSON.stringify({
					type: "login",
					username: this.username,
				})
			);
		};
	}
}
</script>

<style scoped>
.header {
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding-inline: 4em;
	background-color: #131926;
	border-bottom: 2px solid #1b253a;
	max-height: 50px;
}

.header h1 {
	font-size: 1.2em;
	font-weight: normal;
}
</style>
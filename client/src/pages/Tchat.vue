<template>
	<header class="header">
		<div class="header-container">
			<h1>Tchat</h1>
			<p>Connected as {{ username }}</p>
		</div>
	</header>
	<main class="main">
		<div class="tchat">

		</div>
		<div class="input">
			<input type="text" v-model="message" @keyup.enter="sendMessage">
		</div>
	</main>
</template>

<script>
export default {
	name: "Tchat",
	data() {
		return {
			address: this.$route.params.address,
			port: this.$route.params.port,
			username: this.$route.params.username,
			ws: null,
			message: "",
		}
	},
	mounted() {
		if (this.address && this.port) {
			this.connect();
		}
	},
	methods: {
		connect() {
			this.ws = new WebSocket(`ws://${this.address}:${this.port}`);
			this.ws.onopen = () => {
				this.ws.send(
					JSON.stringify({
						type: "login",
						username: this.username,
					})
				);
			};

			this.ws.onmessage = (event) => {
				let data = JSON.parse(event.data);
				switch (data.type) {
					case "message":
						this.gotMessage(data["content"]);
						break;
					case "login":
						this.loggedIn(data["username"]);
						break;
					case "logout":
						this.loggedOut("logout", data["username"]);
						break;
				}
			};
		},
		sendMessage() {
			if (this.message) {
				this.ws.send(
					JSON.stringify({
						type: "message",
						content: this.message,
					})
				);

				this.message = "";
			}
		},
		gotMessage(message) {
			console.log(message);
		},
		loggedIn(username) {
			console.log(username);
		},
		loggedOut(username) {
			console.log(username);
		},
	},
}
</script>

<style scoped>
.header {
	background-color: #131926;
	border-bottom: 2px solid #1b253a;
	max-height: 64px;
	position: fixed;
	width: 100%;
	top: 0;
}

.header-container {
	display: flex;
	align-items: center;
	justify-content: space-between;
	width: min(80%, 1440px);
	margin: 0 auto;
}

.header-container h1 {
	font-size: 1.2em;
	font-weight: normal;
}

.main {
	display: grid;
	flex-direction: row;
	align-items: flex-end;

	margin: auto;
	width: min(80%, 1440px);
	height: 100vh;
}

.input {
	display: flex;
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 64px;
}

.input input {
	border: none;
	border-bottom: 1px solid #1e3348;
	background-color: transparent;
	color: inherit;
	padding: 0.5em;
	width: 60%;
}
</style>
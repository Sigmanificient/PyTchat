<template>
	<header class="header">
		<div class="header-container">
			<h1>Tchat</h1>
			<p>Connected as {{ username }}</p>
		</div>
	</header>
	<div id="tchat" class="container">
		<div class="tchat">
			<div class="message" v-for="message in messages" :key="message">
				{{ message }}
			</div>
		</div>
	</div>
	<div class="input">
		<input type="text" v-model="message" @keyup.enter="sendMessage">
	</div>
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
			messages: [],
			users: [],
			tchat: null,
		}
	},
	mounted() {
		if (this.address && this.port) {
			this.connect();
		}
	},
	methods: {
		connect() {
			this.tchat = document.getElementById("tchat");

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
						this.gotMessage(data["usernames"], data["message"]);
						break;
					case "login":
						this.loggedIn(data["username"]);
						break;
					case "logout":
						this.loggedOut("logout", data["username"]);
						break;
					case "users":
						this.setUsers(data["users"]);
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
		gotMessage(user, message) {
			this.messages.push(
				{
					user: user,
					message: message,
				}
			);

			this.tchat.scrollTop = this.tchat.scrollHeight;
		},
		setUsers(users) {
			this.users = users;
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

.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: calc(100vh - 128px);
	width: 100%;
	overflow-y: scroll;
}

.tchat {
	display: flex;
	flex-direction: column;
	align-items: flex-end;
	margin: auto auto;
	width: min(80%, 1440px);
	height: 100vh;
}

.input {
	background-color: #131926;
	border-top: 2px solid #1b253a;
	position: fixed;
	bottom: 0;
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
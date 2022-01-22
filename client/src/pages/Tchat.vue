<template>
	<header class="header">
		<div class="header-container">
			<h1>Tchat</h1>
			<p>Connected as {{ username }}</p>
		</div>
	</header>
	<div id="tchat" class="container">
		<div class="tchat">
			<div
				class="message-container"
				v-for="message in messages"
				:key="message"
				:class="getMessageClass(message['user'])"
			>
				<div v-if="message['user'] !== 'system'" class="message">
					<p class="author">
						{{ message['user'] }}
					</p>
					<p class="content">
						{{ message['message'] }}
					</p>
				</div>
				<div v-else class="system">
					<p>
						{{ message['message'] }}
					</p>
				</div>
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
						this.gotMessage(data["username"], data["message"]);
						break;
					case "login":
						this.loggedIn(data["username"]);
						break;
					case "logout":
						console.log("logout");
						this.loggedOut("logout", data["username"]);
						break;
					case "users":
						this.setUsers(data["users"]);
						break;
				}
			};
		},
		scrollToBottom() {
			setTimeout(() => {
				this.tchat.scrollTop = this.tchat.scrollHeight;
			}, 1);
		},
		getMessageClass(user) {
			if (user === this.username) {
				return "message-self";
			}
			else if (user === "system") {
				return "message-system";
			}
			else {
				return "message-other";
			}
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
			this.scrollToBottom();
		},
		setUsers(users) {
			this.users = users;
		},
		loggedIn(username) {
			this.messages.push(
				{
					user: "system",
					message: `${username} has joined the chat.`,
				}
			);
			this.scrollToBottom();
		},
		loggedOut(username) {
			this.messages.push(
				{
					user: "system",
					message: `${username} has leaved the chat.`,
				}
			);
			this.scrollToBottom();
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

.message-self {
	justify-content: flex-end;
}

.header-container h1 {
	font-size: 1.2em;
	font-weight: normal;
}

.system {
	margin-top: 10px;
	padding-inline: 10px;
}

.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	height: calc(100vh - 128px);
	width: 100%;
	overflow-y: scroll;
	margin-bottom: 64px;
}

.tchat {
	display: flex;
	flex-direction: column;
	align-items: flex-start;
	justify-content: flex-start;
	margin: auto auto;
	width: min(80%, 1440px);
	height: 100vh;
	gap: 10px;
}

.message-container {
	width: 100%;
	display: flex;
}

.message {
	background-color: #131926;
	border-top: 2px solid #1b253a;
	padding-inline: 10px;
}

.author {
	font-size: 0.6em;
}

.content {
	font-size: 0.8em;
	max-width: 100%;
	word-wrap: break-word;
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
	height: 56px;
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
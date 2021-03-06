<template lang="pug">
.c-question(:class="{queued: hasPermission('room:question.moderate') && question.state === 'mod_queue', 'has-voted': question.voted, pinned: question.is_pinned, archived: question.state === 'archived'}")
	.votes(@click="vote")
		.mdi.mdi-menu-up.upvote
		.vote-count {{ question.score }}
		| Votes
	.content {{ question.content }}
	menu-dropdown(v-if="hasPermission('room:question.moderate')", v-model="modding", strategy="fixed")
		template(v-slot:button="{toggle}")
			bunt-icon-button(@click="toggle") dots-vertical
		template(v-slot:menu)
			.approve-question(v-if="question.state === 'mod_queue'", @click="approveQuestion") {{ $t('Question:moderation-menu:approve-question:label') }}
			.approve-question(v-if="question.state === 'visible'", @click="pinQuestion") {{ $t('Question:moderation-menu:pin-question:label') }}
			.archive-question(v-if="question.state !== 'archived'", @click="archiveQuestion") {{ $t('Question:moderation-menu:archive-question:label') }}
			.unarchive-question(v-if="question.state === 'archived'", @click="unarchiveQuestion") {{ $t('Question:moderation-menu:unarchive-question:label') }}
			.delete-question(@click="deleteQuestion") {{ $t('Question:moderation-menu:delete-question:label') }}
</template>
<script>
import { mapGetters } from 'vuex'
import MenuDropdown from 'components/MenuDropdown'

export default {
	components: { MenuDropdown },
	props: {
		question: Object
	},
	data () {
		return {
			modding: false
		}
	},
	computed: {
		...mapGetters(['hasPermission'])
	},
	created () {},
	mounted () {
		this.$nextTick(() => {
		})
	},
	methods: {
		async vote () {
			this.$store.dispatch('question/vote', this.question)
		},
		async approveQuestion () {
			await this.$store.dispatch('question/approveQuestion', this.question)
			this.modding = false
		},
		async pinQuestion () {
			await this.$store.dispatch('question/pinQuestion', this.question)
			this.modding = false
		},
		async archiveQuestion () {
			await this.$store.dispatch('question/archiveQuestion', this.question)
			this.modding = false
		},
		async unarchiveQuestion () {
			await this.$store.dispatch('question/unarchiveQuestion', this.question)
			this.modding = false
		},
		async deleteQuestion () {
			await this.$store.dispatch('question/deleteQuestion', this.question)
			this.modding = false
		}
	}
}
</script>
<style lang="stylus">
.c-question
	flex: none
	display: flex
	align-items: center
	border-bottom: border-separator()
	position: relative
	.votes
		display: flex
		flex-direction: column
		align-items: center
		padding: 8px
		color: $clr-secondary-text-light
		text-transform: uppercase
		font-size: 12px
		cursor: pointer
		user-select: none
		.mdi
			font-size: 38px
			line-height: 8px
		.vote-count
			font-family: 'Roboto-Condensed'
			font-weight: 200
			font-size: 32px
			line-height: 32px
			color: $clr-primary-text-light
			// TODO scaling for digits
	.content
		flex: auto
		margin: 8px
	&.queued
		$clr-queued = alpha($clr-black, .05)
		background: repeating-linear-gradient(-45deg, transparent, transparent 10px, $clr-queued 10px, $clr-queued 20px, transparent 20px)
		&::after
			content: 'needs approval'
			display: block
			position: absolute
			right: 8px
			top: 8px
			font-size: 12px
			color: $clr-deep-orange
			font-weight: 600
	&.has-voted
		.votes
			color: $clr-green-700
			.vote-count
				color: $clr-green-800
	&.pinned
		border: 4px solid var(--clr-primary)
		border-bottom: none
		border-top: none
	&.archived
		background-color: $clr-grey-200
		color: $clr-disabled-text-light
		.votes, .vote-count
			color: $clr-disabled-text-light
		&::after
			content: 'archived'
			display: block
			position: absolute
			right: 8px
			top: 8px
			font-size: 12px
			color: $clr-secondary-text-light
			font-weight: 600
	.c-menu-dropdown .menu
		color: $clr-primary-text-light
		.delete-question
			color: $clr-danger
			&:hover
				background-color: $clr-danger
				color: $clr-primary-text-dark
</style>

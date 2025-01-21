--% index/fmus
.,d
	?pick
		$*code __FILE__
		@docker + kubernetes*
			?pick
				@dockerfile*
				@docker-compose*
				@kubernetes*
		@automation: terrafor, ansible, chef, puppet*
			?pick
				@terraform*
				@ansible*
		@aws*
		@gcp*
		@azure*
		@heroku*
		@netlify*
		@vercel*
		@monorepo - turborepo, nx*
			?pick
				@turborepo: https://turborepo.org/docs, https://github.com/vercel/turborepo*
				@nx: https://nx.dev/, https://github.com/nrwl/nx*
		@register API - tw, fb, ig, gh*
			?pick
				@twitter app*
				@facebook app*
				@instagram app*
				@github token*
		@ci/cd - gitlab, github, jenkins, circle, travis, argo*
			?pick
				@gitlab-ci*
				@github actions*
				@jenkins*
				@circle ci*
				@travis ci*
				@argo cd*
		@logging/monitoring - datadog, elk*
			?pick
				@datadog*
				@ELK*
		@selenium*
			?pick
				@selenium python*
				@selenium java*
		@data science/engineering, ml/ai*
			?pick
				@machine learning*
					?pick
						@supervised*
						@unsupervised*
				@deep learning*
				@spark / bigdata*
				@opencv*
--#

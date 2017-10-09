#!/bin/bash

set -eu

git remote add heroku https://git.heroku.com/$HEROKU_APP_NAME.git

cat > ~/.netrc << EOF
machine api.heroku.com
	login $HEROKU_LOGIN
	password $HEROKU_API_KEY
machine git.heroku.com
	login $HEROKU_LOGIN
	password $HEROKU_API_KEY
EOF

# Add heroku.com to the list of known hosts
ssh-keyscan -H heroku.com >> ~/.ssh/known_hosts

# Use the official Jekyll image from Docker Hub
# Using a specific version is good practice for reproducibility
FROM jekyll/jekyll:3.9

# Set the working directory inside the container
WORKDIR /srv/jekyll

# Copy the Gemfile and Gemfile.lock to the container
# This is done first to leverage Docker's layer caching.
# The bundle install step will only re-run if the Gemfile changes.
COPY Gemfile Gemfile.lock* ./

# Install the Ruby gems specified in the Gemfile
RUN bundle install

# Copy the rest of your Jekyll site's source code into the container
COPY . .

# Expose port 4000 to allow external access to the Jekyll server
EXPOSE 4000

# Command to run when the container starts.
# This builds the site and serves it, listening on all network interfaces.
CMD ["jekyll", "serve", "--host", "0.0.0.0"]
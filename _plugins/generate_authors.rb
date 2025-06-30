# _plugins/generate_authors.rb

module Jekyll
    class AuthorPage < Page
      def initialize(site, base, dir, member)
        @site = site
        @base = base
        @dir = dir       # e.g. 'author/andy-berry'
        @name = 'index.html'

        self.process(@name)
        self.read_yaml(File.join(base, '_layouts'), 'author.html')

        self.data['title'] = member['name']
        self.data['slug'] = member['slug']
        self.data['role'] = member['role']
        self.data['email'] = member['email']
        self.data['pure_url'] = member['pure_url']
        self.data['orcid'] = member['orcid']
        self.data['bio'] = member['bio']
        self.data['image'] = member['image']
        self.data['research_interests'] = member['research_interests']
      end
    end

    class AuthorPageGenerator < Generator
      safe true

      def generate(site)
        team_data = site.data.dig('team', 'members')
        if team_data.nil? || !team_data.is_a?(Array) || team_data.empty?
          Jekyll.logger.warn "Author Generator:", "No team members found in _data/team.yml"
          return
        end

        team_data.each do |member|
          next unless member['slug'] && !member['slug'].empty?

          slug = member['slug']
          dir = File.join('author', slug)

          Jekyll.logger.info "Author Generator:", "Generating author page for #{member['name']} at /#{dir}/"

          site.pages << AuthorPage.new(site, site.source, dir, member)
        end
      end
    end
  end

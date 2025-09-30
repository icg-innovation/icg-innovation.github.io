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
        # Try the flat members list first (for backward compatibility)
        team_data = site.data.dig('team', 'members')
        
        # If no flat list, generate from teams structure
        if team_data.nil? || !team_data.is_a?(Array) || team_data.empty?
          team_data = []
          teams_data = site.data.dig('team', 'teams')
          
          if teams_data && teams_data.is_a?(Hash)
            teams_data.each do |team_name, team_info|
              if team_info && team_info['members'] && team_info['members'].is_a?(Array)
                team_data.concat(team_info['members'])
              end
            end
          end
        end
        
        if team_data.empty?
          Jekyll.logger.warn "Author Generator:", "No team members found in _data/team.yml"
          return
        end

        Jekyll.logger.info "Author Generator:", "Found #{team_data.length} team members"

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

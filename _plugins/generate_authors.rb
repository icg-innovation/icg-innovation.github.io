# _plugins/generate_authors.rb

module Jekyll
    class AuthorPageGenerator < Generator
      safe true
  
      def generate(site)
        # Loop over each team member from the data file
        site.data["team"]["members"].each do |member|
          # Build a slug
          slug = member["name"].downcase.strip.gsub(" ", "-").gsub(/[^\w-]/, "")
          
          # Create a new document for the collection
          author_doc = Jekyll::Document.new(
            File.join(site.source, "_authors", "#{slug}.md"),
            site: site,
            collection: site.collections["authors"]
          )
  
          # Front matter for the author page
          author_doc.data["layout"] = "author"
          author_doc.data["title"] = member["name"]
          author_doc.data["slug"] = slug
          author_doc.data["role"] = member["role"]
          author_doc.data["email"] = member["email"]
          author_doc.data["pure_url"] = member["pure_url"]
          author_doc.data["orcid"] = member["orcid"]
          author_doc.data["bio"] = member["bio"]
          author_doc.data["image"] = member["image"]
          author_doc.data["research_interests"] = member["research_interests"]
  
          # Save it into the collection
          site.collections["authors"].docs << author_doc
        end
      end
    end
  end
  
# Plugin to generate a flat members list from the team structure
# This maintains backward compatibility while eliminating duplication

Jekyll::Hooks.register :site, :post_read do |site|
  # Get the team data
  teams_data = site.data['team']['teams']
  
  if teams_data
    # Initialize empty members array
    members = []
    previous_members = []
    
    # Iterate through each team and collect all members
    teams_data.each do |team_key, team_data|
      if team_data['members']
        team_data['members'].each do |member|
          if team_key == 'previous'
            # Mark previous members and add to separate list
            member_copy = member.dup
            member_copy['is_previous'] = true
            previous_members << member_copy
            # Also add to main list for full backward compatibility
            members << member_copy
          else
            members << member
          end
        end
      end
    end
    
    # Add the flat members list to site.data.team.members
    site.data['team']['members'] = members
    
    # Add separate previous members list for potential future use
    site.data['team']['previous_members'] = previous_members
    
    # Optional: Log the number of members generated
    Jekyll.logger.info "Generated flat members list:", "#{members.length} total members (#{previous_members.length} previous) from #{teams_data.length} teams"
  end
end
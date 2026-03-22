import csv
import os

# Define the CSV file path
csv_file = "sprint_data.csv"

def read_from_csv():
    """Read and display data from CSV file"""
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            # Display header
            if rows:
                print(f"\n{'Sprint':<10} {'Story':<25} {'Status':<15} {'StoryPoints':<12} {'Blocked':<8}", end="")
                if len(rows[0]) > 5:
                    print(f" {'SprintStatus':<10}")
                else:
                    print()
                print("=" * 100)
                
                # Display data rows
                for row in rows[1:]:
                    if len(row) >= 5:
                        print(f"{row[0]:<10} {row[1]:<25} {row[2]:<15} {row[3]:<12} {row[4]:<8}", end="")
                        if len(row) > 5:
                            print(f" {row[5]:<10}")
                        else:
                            print()
        
        print(f"\n✓ Total rows in CSV: {len(rows) - 1}")
        return True
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return False

def get_sprint_summary():
    """Display summary statistics from CSV"""
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        if len(rows) > 1:
            print("\n" + "=" * 100)
            print("SPRINT SUMMARY")
            print("=" * 100)
            
            sprints = {}
            for row in rows[1:]:
                if len(row) >= 4:
                    sprint = row[0]
                    status = row[2]
                    story_points = int(row[3]) if row[3].isdigit() else 0
                    
                    if sprint not in sprints:
                        sprints[sprint] = {"Done": 0, "In Progress": 0, "To Do": 0, "Total": 0}
                    
                    sprints[sprint]["Total"] += story_points
                    sprints[sprint][status] = sprints[sprint].get(status, 0) + story_points
            
            for sprint in sorted(sprints.keys()):
                stats = sprints[sprint]
                completion = (stats["Done"] / stats["Total"] * 100) if stats["Total"] > 0 else 0
                print(f"{sprint}: {stats['Done']}/{stats['Total']} pts ({completion:.0f}%) - In Progress: {stats['In Progress']} pts, To Do: {stats['To Do']} pts")
        
        return True
    except Exception as e:
        print(f"✗ Error generating summary: {e}")
        return False

if __name__ == "__main__":
    print("\n" + "=" * 100)
    print("AI SCRUM ASSISTANT - SPRINT DATA VIEWER")
    print("=" * 100)
    
    # Read and display data from CSV
    read_from_csv()
    
    # Display summary
    get_sprint_summary()
    
    print("\n" + "=" * 100)

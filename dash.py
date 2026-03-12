import os 
import subprocess
from google import genai
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
client= genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_git_diff(): 
    #"captures the staged changes (git add) in the current repo"
    try: 
        diff= subprocess.check_output(['git','diff','--cached'],text=True)
        return diff if diff else None
    except subprocess.CalledProcessError:
        return "Error: Ensure you are in a Git Repository"
    
def generate_commit_message(diff_text):
    #"Send the diff to OpenAI with specific Prompt Engineering instructions ."
    system_prompt= ( " You are a technical assistant that writes Git Commit Message."
                    "Use the conventional commits format (e.g, feat:add login logic)."
                    "Focus on 'why' and 'what', not 'how'. Be concise. "
                    "Output only the commit message itself, no extra text or quotes."
                    "If the changes are strictly UI-related, start with 'feat(ui)'. if they are logic-related, start with a 'fix'."
                    "Analyze the modified function names and variable changes. if a function named calculate_tax was changed ,ensure the commit message mentions the tax logic."

                    )
   # Gemini combines instructions and data into one prompt or uses a specific system_instruction parameter
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=f"{system_prompt}\n\nGenerate a commit message for this diff:\n\n{diff_text}"
)
    return response.text

def main():
    diff=get_git_diff()
    if not diff:
        print("No changes stages. Run 'git add <file>' first.")
        return
    print("Analyzing your changes...")
    suggestion =generate_commit_message(diff)
    print(f"\nSuggested Commit Message:\n\n {suggestion}\n")
    # ... after your print statement ...
    
    confirm = input("Do you want to commit with this message? (y/n): ").lower()
    
    if confirm == 'y':
        try:
            # This line actually runs the git command for you
            subprocess.run(['git', 'commit', '-m', suggestion], check=True)
            print("✅ Successfully committed to your repository!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error committing: {e}")
    else:
        print("Commit cancelled.")
if __name__ == "__main__":
    main()
    
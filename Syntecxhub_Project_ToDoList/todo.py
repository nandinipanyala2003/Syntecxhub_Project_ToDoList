import json
import os
from datetime import datetime

TASKS_FILE = 'tasks.json'

def load_tasks():
    """JSON file nunchi tasks load cheyyi"""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    """Tasks JSON file ki save"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    """New task add"""
    task = input("Task enter cheyyi: ").strip()
    if task:
        priority = input("Priority (H/M/L) [M]: ").strip().upper() or 'M'
        tasks.append({
            'task': task,
            'priority': priority,
            'done': False,
            'added': datetime.now().strftime('%Y-%m-%d %H:%M')
        })
        save_tasks(tasks)
        print(f"✅ '{task}' ({priority}) added! Total: {len(tasks)}")
    else:
        print("❌ Empty task!")

def view_tasks(tasks):
    """Tasks display (priority + done status)"""
    if not tasks:
        print("📭 No tasks!")
        return
    
    print("\n📋 TO-DO LIST:")
    print("-" * 60)
    for i, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "⏳"
        print(f"{i:2d}. {status} [{t['priority']}] {t['task']:<30} {t.get('added', '')}")
    print("-" * 60)

def mark_done(tasks):
    """Task complete mark"""
    view_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Complete task number: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]['done'] = True
                save_tasks(tasks)
                print("✅ Marked as done!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Number enter!")

def delete_task(tasks):
    """Task delete"""
    view_tasks(tasks)
    if tasks:
        try:
            idx = int(input("Delete task number: ")) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                save_tasks(tasks)
                print(f"🗑️ '{removed['task']}' deleted! Total: {len(tasks)}")
            else:
                print("❌ Invalid!")
        except ValueError:
            print("❌ Number raa!")

def main():
    """Main menu loop"""
    tasks = load_tasks()
    print("🔥 SYNTECXHUB TODO LIST MANAGER")
    
    while True:
        print("\n📱 MENU:")
        print("1. ➕ Add Task")
        print("2. 📋 View Tasks") 
        print("3. ✅ Mark Done")
        print("4. 🗑️ Delete Task")
        print("5. 📊 Stats")
        print("0. ❌ Quit")
        
        try:
            choice = input("Choose (0-5): ").strip()
            
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                view_tasks(tasks)
            elif choice == '3':
                mark_done(tasks)
            elif choice == '4':
                delete_task(tasks)
            elif choice == '5':
                done = sum(1 for t in tasks if t['done'])
                print(f"📊 Stats: {len(tasks)} total, {done} done, {len(tasks)-done} pending")
            elif choice == '0':
                print("👋 Bye! Tasks saved in tasks.json")
                break
            else:
                print("❌ Invalid! 0-5 choose")
                
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            break

if __name__ == "__main__":
    main()

import { invoke } from '@tauri-apps/api/tauri';

async function greet(name: string) {
  const result = await invoke<string>('greet', { name });
  console.log(result);
}

greet('Alice');

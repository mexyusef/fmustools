import { Command } from '@oclif/core';

export default class Greet extends Command {
  static description = 'Greet the user';

  async run() {
    const name = 'John'; // Replace with your desired name

    this.log(`Hello, ${name}!`);
  }
}

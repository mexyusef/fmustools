import { CLI } from 'cli-ux';

export class MyCli extends CLI {
  static description = 'My CLI description';
  static flags = {};

  // ...
}

MyCli.run().catch(CLI.handleError);

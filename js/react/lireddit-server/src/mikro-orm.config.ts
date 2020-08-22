import { Post } from './entities/Post';
import { __prod__ } from './constants';
import { MikroORM } from '@mikro-orm/core';

export default {
  entities: [Post],
  dbName: 'lireddit',
  user: 'postgres',
  password: 'postgres',
  debug: !__prod__,
  type: 'postgresql',
} as Parameters<typeof MikroORM.init>[0];

"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const Post_1 = require("./entities/Post");
const constants_1 = require("./constants");
exports.default = {
    entities: [Post_1.Post],
    dbName: 'lireddit',
    user: 'postgres',
    password: 'postgres',
    debug: !constants_1.__prod__,
    type: 'postgresql',
};
//# sourceMappingURL=mikro-orm.config.js.map
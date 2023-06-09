// Copyright 2017 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "src/objects/visitors.h"

#include "src/codegen/reloc-info.h"

#include "src/objects/fixed-array-inl.h"

namespace v8 {
namespace internal {

const char* RootVisitor::RootName(Root root) {
  switch (root) {
#define ROOT_CASE(root_id, description) \
  case Root::root_id:                   \
    return description;
    ROOT_ID_LIST(ROOT_CASE)
#undef ROOT_CASE
    case Root::kNumberOfRoots:
      break;
  }
  UNREACHABLE();
}

void ObjectVisitor::VisitRelocInfo(RelocIterator* it) {
  for (; !it->done(); it->next()) {
    it->rinfo()->Visit(this);
  }
}

}  // namespace internal
}  // namespace v8

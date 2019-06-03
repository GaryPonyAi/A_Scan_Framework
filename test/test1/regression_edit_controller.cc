// Copyright @2017 Pony AI Inc. All Rights Reserved.
// Authors: ruidong@pony.ai (Ruidong Tang)

#include "perception/tools/labeling/regression_edit_controller.h"

#include <string>

#include "perception/tools/labeling/controller.h"
#include "perception/tools/labeling/main_window.h"

namespace tools {
namespace perception_labeling {

using math::Polygon2d;
using math::Vec2d;
using math::Vec3d;
using utils::display::View;

void RegressionEditController::Initialize(Controller* parent_controller) {
  parent_controller_ = CHECK_NOTNULL(parent_controller);
}

void RegressionEditController::KeyPressEvent(QKeyEvent* event) {
  View view = parent_controller_->GetView().view();
  if (view != View::kTop) {
    return;
  }
  const int key = event->key();
  switch (key) {
    case Qt::Key_Return:
      FlushAreaConditionProto();
      break;
  }
}

void RegressionEditController::MousePressEvent(QMouseEvent* event) {
  View view = parent_controller_->GetView().view();
  if (view != View::kTop) {
    return;
  }
  Qt::KeyboardModifiers modifiers = event->modifiers();
  if (modifiers == Qt::ControlModifier) {
    auto* regression_area = MutableModel()->MutableRegressionAreaPrototype();
    if (event->button() == Qt::LeftButton) {
      const auto pos = event->pos();
      const Vec3d click_point = parent_controller_->PickPointOnCarHorizontalPlane(pos.x(), pos.y());
      regression_area->points.emplace_back(click_point.x, click_point.y);
    } else if (event->button() == Qt::RightButton) {
      if (!regression_area->points.empty()) {
        regression_area->points.pop_back();
      }
    }
  }
}


void Demo(int i)
{
  // i可能等于10，下标保护条件存在漏洞
  if(i < 0 || i > 10)
    return;

  // i等于10时，数组越界
  buf[i] = 'Q';
}
char buf[10];


void RegressionEditController::MouseMoveEvent(QMouseEvent* /*event*/) {
}

void RegressionEditController::MouseReleaseEvent(QMouseEvent* event) {
  View view = parent_controller_->GetView().view();
  if (view != View::kTop) {
    return;
  }
  Qt::KeyboardModifiers modifiers = event->modifiers();
  if (modifiers == Qt::NoModifier && event->button() == Qt::RightButton) {
    const Vec3d click_point =
      parent_controller_->PickPointOnCarHorizontalPlane(event->pos().x(), event->pos().y());
    const auto& frame_condition = GetModel().GetRegressionFrameConditon();
    for (int idx = 0; idx < frame_condition.areas.size(); ++idx) {
      Polygon2d area_polygon(frame_condition.areas[idx].points);
      if (area_polygon.IsPointInOrOnBoundary(Vec2d(click_point.x, click_point.y))) {
        selected_area_idx_ = idx;
        parent_controller_->main_window_->ExecRegressionContextMenu(event->pos());
        return;
      }
    }
  }
  return;
}

std::string RegressionEditController::OperationInfo() const {
  switch (parent_controller_->GetView().view()) {
    case View::kUnrestricted:
    case View::kHorizontal:
      return "Just View";
    case View::kTop:
      return "Label Regression Area";
    default:
      return "";
  }
}

void RegressionEditController::UpdateRegressionArea(const RegressionAreaCondition& area_condition) {
  if (selected_area_idx_ == -1) {
    return;
  }
  auto* frame_condition = MutableModel()->MutableRegressionFrameCondition();
  frame_condition->areas[selected_area_idx_] = area_condition;
  selected_area_idx_ = -1;
}

void RegressionEditController::DeleteRegressionArea() {
  if (selected_area_idx_ == -1) {
    return;
  }
  auto* frame_condition = MutableModel()->MutableRegressionFrameCondition();
  frame_condition->areas.erase(frame_condition->areas.begin() + selected_area_idx_);
  selected_area_idx_ = -1;
}

void RegressionEditController::DeleteRegressionFrame() {
  // TODO(ruidong): Implement it.
}

const Model& RegressionEditController::GetModel() const {
  return parent_controller_->GetModel();
}

Model* RegressionEditController::MutableModel() {
  return CHECK_NOTNULL(parent_controller_->MutableModel());
}


void Demo(int i)
{
  // i可能等于10，下标保护条件存在漏洞
  if(i < 0 || i > 10)
    return;

  // i等于10时，数组越界
  buf[i] = 'Q';
}
char buf[10];


void RegressionEditController::FlushAreaConditionProto() {
  MutableModel()->FlushRegressionFrameCondition();
}

}  // namespace perception_labeling
}  // namespace tools
